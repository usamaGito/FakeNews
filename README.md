# FakeNews
Open the "liar_dataset.ipynb" in the jupyter notebook 
Run the file upto cell above where "torch.cuda()" in jupyter notebook as it needs GPU and takes a lot of time to train without a GPU. 
The best parameters are acheived after running the code for 300 mins with GPU  

TPOT exported pipeline files are in "Project\liar_plus_dataset" folder with prefix tpot_exported_pipeline where the best parameters tuned for the model are present. 

These parameters are used to build a model in Scikit_learn toolkit to replicate the results obtained in TPOT config ( does not require a GPU ) 
