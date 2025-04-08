FROM maven:3.8.1-openjdk-11 AS build

WORKDIR /app

COPY pom.xml .

RUN mvn dependency:go-offline

COPY src ./src

RUN mvn package

FROM openjdk:11-jre-slim

WORKDIR /app

COPY --from=build /app/target/kovendhan-jenkins-1.0-SNAPSHOT.jar kovendhan-jenkins.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "kovendhan-jenkins.jar"]
