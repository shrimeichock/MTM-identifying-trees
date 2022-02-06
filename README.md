# MTM-identifying-trees


## Steps:

1. Download Anaconda https://www.anaconda.com/products/individual
2. In the Anacona Prompt, enter the following commands:

    Create a python environment
    ```
    conda create -n pyEnv python=3.9
    conda activate pyEnv
    ```
    
    Install libraries
    ```
    conda install -c conda-forge opencv
    conda install -c conda-forge matplotlib
    conda install -c conda-forge spyder
    ```
    
    Launch Spyder:
    ```
    spyder
    ```
3. Download or clone this repository to run the source code on spyder.

## Input Image Requirements:

1. Use PNG for more accurate results.
2. Image must be 800m by 800m (64 hectares).
3. Hue will need to be adjusted according to the image (Example images and hues can be found in the test_image directory).


## Output:

The program outputs 
* an image with tree areas surrounded by either green or red
* the final area

The areas in green are less than 1 hectare and are included in the final area.

The areas in red are larger than 1 hectare, which are not included in the final area.


## Contributors:

* Shrimei Chock
* Maisha Abdullah
* Thanuja Sivaananthan
