# push-gvmi
Automating the building and pushing parts of working with GVMI images

## What you need to do:
 - First, go to Settings > Secrets > Actions > New repository secret and create a `SKYNET_REGISTRY_SEED` secret. This can be anything, really. Words, a hash, a phrase, a password, you name it.
![image](https://user-images.githubusercontent.com/64747030/174495772-98614fdf-9e7f-4a50-99cc-e3ce40459d6a.png)

 - Then, create your [/.github/workflows/push-gvmi.yml](https://github.com/figurestudios/push-gvmi/blob/main/.github/workflows/push-gvmi.yml) file.
 - Now change the skylink on [this line](https://github.com/figurestudios/push-gvmi/blob/main/get-parse_hash.py#L7) to the marked text below, taken from the workflow's successful run (navigate [here](https://github.com/figurestudios/push-gvmi/actions) & click the top one). This skylink will never change, so you just need to do it when you create your new project.
![image](https://user-images.githubusercontent.com/64747030/174495407-960f9937-ca8c-4abf-abe9-85e51fdf83c5.png)
 - To get your automatically updating image hash, run `await get_hash()`

## Requirements:
 - Must be on a 'main' branch.
 - Must have a Dockerfile at the root of your repository.
 - Install the Skynet dependency: `pip install siaskynet`
 - Install the aiofiles dependency: `pip install aiofiles`
