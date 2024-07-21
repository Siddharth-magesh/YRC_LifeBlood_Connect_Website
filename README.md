# YRC_LifeBlood_Connect_Website
BloodBridge-Platform seamlessly connects donors with recipients, streamlining the blood donation process to save lives.

## Installation and setting up the env

1. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/Siddharth-magesh/YRC_LifeBlood_Connect_Website.git
    ```
    This command creates a local copy of the YRC_LifeBlood_Connect project on your machine.


2. Create a new conda environment with Python 3.10:
    ```bash
    conda create yrc python=3.10
    ```
    
3. Activate the newly created environment:
   ```bash
    conda activate yrc
    ```
    This command activates the `yrc` environment so that subsequent commands run within this context.

4. Navigate to the project directory:
    ```bash
    cd YRC_LifeBlood_Connect_Website
    ```
    change to your working directory.

5. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    This installs all the necessary libraries and dependencies listed in the `requirements.txt` file.

## Running the application
> [!NOTE]
> Make sure you have an active environment and all the requirements have been installed

1. Create a `.env` file with `SECRET_KEY` and `DATABASE_URI`
    ```bash
    touch .env
    ```
    write the `SECRET_KEY` and `DATABASE_URI` in the file

2. Run the web app by using the command
   In linux,

   ```bash
   flask run --debug
   ```
   In windows,
   ```bash
   python -m flask run --debug
   ```
   This will run the app on localhost in your computer.

