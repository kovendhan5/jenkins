# Use an official Maven image to build the application
FROM maven:3.8.1-openjdk-11 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the pom.xml file to download dependencies
COPY pom.xml .

# Download all dependencies
RUN mvn dependency:go-offline

# Copy the entire source code to the working directory
COPY src ./src

# Build the application
RUN mvn package

# Use an official OpenJDK runtime as a base image
FROM openjdk:11-jre-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the JAR file from the build stage
COPY --from=build /app/target/kovendhan-jenkins-1.0-SNAPSHOT.jar kovendhan-jenkins.jar

# Expose the application port
EXPOSE 8080

# Command to run the application
ENTRYPOINT ["java", "-jar", "kovendhan-jenkins.jar"]
