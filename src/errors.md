# error 1
```
Container] 2024/12/01 18:26:28.430606 Running on CodeBuild On-demand
[Container] 2024/12/01 18:26:28.430617 Waiting for agent ping
[Container] 2024/12/01 18:26:28.531704 Waiting for DOWNLOAD_SOURCE
[Container] 2024/12/01 18:26:30.251539 Phase is DOWNLOAD_SOURCE
[Container] 2024/12/01 18:26:30.284018 CODEBUILD_SRC_DIR=/codebuild/output/src1581154250/src
[Container] 2024/12/01 18:26:30.284603 YAML location is /codebuild/output/src1581154250/src/buildspec.yml
[Container] 2024/12/01 18:26:30.286804 Setting HTTP client timeout to higher timeout for S3 source
[Container] 2024/12/01 18:26:30.287075 Processing environment variables
[Container] 2024/12/01 18:26:30.481786 Selecting 'java' runtime version 'corretto11' based on manual selections...
[Container] 2024/12/01 18:26:30.481803 Selecting 'docker' runtime version '20' based on manual selections...
[Container] 2024/12/01 18:26:30.481818 Phase complete: DOWNLOAD_SOURCE State: FAILED
[Container] 2024/12/01 18:26:30.481831 Phase context status code: YAML_FILE_ERROR Message: Unknown runtime named 'docker'. This build image has the following runtimes: dotnet, golang, java, nodejs, php, python, ruby
```

# error 2
```
[Container] 2024/12/01 18:38:49.254021 Running on CodeBuild On-demand
[Container] 2024/12/01 18:38:49.254045 Waiting for agent ping
[Container] 2024/12/01 18:38:49.455937 Waiting for DOWNLOAD_SOURCE
[Container] 2024/12/01 18:38:51.416590 Phase is DOWNLOAD_SOURCE
[Container] 2024/12/01 18:38:51.454707 CODEBUILD_SRC_DIR=/codebuild/output/src1657406599/src
[Container] 2024/12/01 18:38:51.455275 YAML location is /codebuild/output/src1657406599/src/buildspec.yml
[Container] 2024/12/01 18:38:51.461128 Phase complete: DOWNLOAD_SOURCE State: FAILED
[Container] 2024/12/01 18:38:51.461185 Phase context status code: YAML_FILE_ERROR Message: Expected Commands[4] to be of string type: found subkeys instead at line 10, value of the key tag on line 9 might be empty
```

# error 3 
```
#6 [3/3] COPY target/policy-service-0.0.1-SNAPSHOT.jar app.jar
#6 ERROR: failed to calculate checksum of ref 51ec7ffb-a83e-4ca6-8833-a5cb92035ae9::u0t9z8205qj8w4njsf6c4dx94: failed to walk /var/lib/docker/tmp/buildkit-mount1314270090/target: lstat /var/lib/docker/tmp/buildkit-mount1314270090/target: no such file or directory
#7 [1/3] FROM docker.io/library/openjdk:17-jdk-alpine@sha256:4b6abae565492dbe9e7a894137c966a7485154238902f2f25e9dbd9784383d81
#7 resolve docker.io/library/openjdk:17-jdk-alpine@sha256:4b6abae565492dbe9e7a894137c966a7485154238902f2f25e9dbd9784383d81 0.0s done
#7 sha256:4b6abae565492dbe9e7a894137c966a7485154238902f2f25e9dbd9784383d81 319B / 319B done
#7 sha256:a996cdcc040704ec6badaf5fecf1e144c096e00231a29188596c784bcf858d05 951B / 951B done
#7 sha256:264c9bdce361556ba6e685e401662648358980c01151c3d977f0fdf77f7c26ab 3.48kB / 3.48kB done
#7 CANCELED
------
 > [3/3] COPY target/policy-service-0.0.1-SNAPSHOT.jar app.jar:
------
Dockerfile:8
--------------------
   6 |     
   7 |          # Copy the JAR file into the container
   8 | >>>      COPY target/policy-service-0.0.1-SNAPSHOT.jar app.jar
   9 |     
  10 |          # Expose the port the app runs on
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref 51ec7ffb-a83e-4ca6-8833-a5cb92035ae9::u0t9z8205qj8w4njsf6c4dx94: failed to walk /var/lib/docker/tmp/buildkit-mount1314270090/target: lstat /var/lib/docker/tmp/buildkit-mount1314270090/target: no such file or directory
[Container] 2024/12/01 20:14:26.770996 Command did not exit successfully docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG . exit status 1

```

# error 4

```
Container] 2024/12/01 20:19:30.641152 Running command chmod +x mvnw
[Container] 2024/12/01 20:19:30.648059 Running command ./mvnw clean package -DskipTests
./mvnw: line 114: ./.mvn/wrapper/maven-wrapper.properties: No such file or directory
[Container] 2024/12/01 20:19:30.655241 Command did not exit successfully ./mvnw clean package -DskipTests exit status 1
[Container] 2024/12/01 20:19:30.659434 Phase complete: BUILD State: FAILED
[Container] 2024/12/01 20:19:30.659450 Phase context status code: COMMAND_EXECUTION_ERROR Message: Error while executing command: ./mvnw clean package -DskipTests. Reason: exit status 1
```

# error 5
```
(base) unmeshmali@Unmeshs-MacBook-Pro yoda-insurance-ms % aws eks list-clusters

An error occurred (AccessDeniedException) when calling the ListClusters operation: User: arn:aws:iam::550432870296:user/um-caltechCC-user is not authorized to perform: eks:ListClusters on resource: arn:aws:eks:us-east-1:550432870296:cluster/*
(base) unmeshmali@Unmeshs-MacBook-Pro yoda-insurance-ms % kubectl get configmap aws-auth -n kube-system
error: You must be logged in to the server (Unauthorized)
```