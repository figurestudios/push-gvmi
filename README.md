# push-gvmi
Automating the building and pushing parts of working with GVMI images

## What you need to do:
 - First, go to Settings > Secrets > Actions > New repository secret and create a `SKYNET_REGISTRY_SEED` secret. This can be anything, really. Words, a hash, a phrase, a password, you name it.
![image](https://user-images.githubusercontent.com/64747030/174495772-98614fdf-9e7f-4a50-99cc-e3ce40459d6a.png)

 - Then, create your [/.github/workflows/push-gvmi.yml](https://github.com/figurestudios/push-gvmi/blob/main/.github/workflows/push-gvmi.yml) file.
 - Optionally change these lines {[20](https://github.com/figurestudios/push-gvmi/blob/main/.github/workflows/push-gvmi.yml#L20), [22](https://github.com/figurestudios/push-gvmi/blob/main/.github/workflows/push-gvmi.yml#L22), [23](https://github.com/figurestudios/push-gvmi/blob/main/.github/workflows/push-gvmi.yml#L23), [25](https://github.com/figurestudios/push-gvmi/blob/main/.github/workflows/push-gvmi.yml#L25)} to give the Docker image a more fitting name.
 - Now change the skylink on [this line](https://github.com/figurestudios/push-gvmi/blob/main/get-parse_hash.py#L5) to the marked text below, taken from the workflow's successful run. This skylink will never change, so you just need to do it when you create your new project.
![image](https://user-images.githubusercontent.com/64747030/174495407-960f9937-ca8c-4abf-abe9-85e51fdf83c5.png)
 - `line[line.find('link ')+5:]` on [line 12](https://github.com/figurestudios/push-gvmi/blob/main/get-parse_hash.py#L12) is your image hash. Feel free to use this directly in your project.

## Requirements:
 - Must be on a 'main' branch.
 - Must have a Dockerfile at the root of your repository.
