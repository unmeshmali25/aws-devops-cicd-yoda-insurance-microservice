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