     # Use a base image with Java
     FROM openjdk:17-jdk-alpine

     # Set the working directory
     WORKDIR /app

     # Copy the JAR file into the container
     COPY target/policy-service-0.0.1-SNAPSHOT.jar app.jar

     # Expose the port the app runs on
     EXPOSE 8080

     # Run the JAR file
     ENTRYPOINT ["java", "-jar", "app.jar"]