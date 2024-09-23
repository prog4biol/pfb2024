# Create this Repo

To create this repo I duplicated last year's repo with these notes:  
https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository

1. Create a new empty repository on github.com for the new copy
2. Open Terminal.  
3. Create a bare clone of the repository.  
   ```
   OLD_REPO_NAME=pfb2023.git
   OLD_REPO_URL=https://github.com/prog4biol/$OLD_REPO_NAME
   git clone --bare $OLD_REPO_URL
   ```  
4. Mirror-push to the new repository.  
   ```
   NEW_REPO_NAME=pfb2024.git
   NEW_REPO_GIT=https://github.com/prog4biol/$NEW_REPO_NAME
   cd $OLD_REPO_NAME 
   git push --mirror $NEW_REPO_GIT
   ```
5. Remove the temporary local repository you created earlier.  
    ```
    cd ..
    rm -rf $OLD_REPO_NAME
   ```
