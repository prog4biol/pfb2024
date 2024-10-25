# Image Processing with Jay Unruh

1. Open a Finder window and navigate to the `/Applications` folder, then double-click on the JupyterLab icon to launch the desktop application.

2. At the bottom of the JupyterLab desktop application panel, where it says "Python environment not found," click the "Install using the bundled installer" link, then wait while JupyterLab builds a new environment.

3. When the JupyterLab environment finishes building, click "New Session..." under the **Start** section to begin a new jupyter notebook session.

4. Open a new Terminal window and do the following:
    ```bash
    mamba activate -p $HOME/Library/jupyterlab-desktop/jlab_server
    mamba install -c conda-forge jupyter numpy pandas scipy matplotlib tifffile pillow
    ```
    
5. In JupyterLab, click the "Python 3 (ipykernel)" button under the **Notebook** section to start a new Jupyter Notebook, then insert the following lines into the code block:
    ```python
    import numpy
    import scipy
    import matplotlib
    import pandas
    import PIL
    import tifffile
    ```

6. Press `control`+`Return` to execute the code block. If you do not receive any errors, your install was successful.


__STOP HERE for the Jupyter Notebook intro__

1. In your Terminal window, navigate somewhere outside of any Git repositories and clone Jay's workshop repository from GitHub: 
    ```bash
    cd ~
    mkdir image_processing
    
    git clone https://github.com/jayunruh/python_IP_course.git
    cd python_IP_course
    ```


