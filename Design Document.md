# Fake Review Generator

## Design Document

<table>
  <tr>
    <td>Overview</td>
    <td>Generate </td>
  </tr>
  <tr>
    <td>Top Questions</td>
    <td>Question: 
How to generate fake reviews by learning from a dataset of Amazon food and music reviews?
How 
</td>
  </tr>
  <tr>
    <td>Use Cases</td>
    <td><Toan>
UC1 - Prepare the data and make sure it is compatible with the training pipeline.
UC2 - Train the model. User provides a dataset and the script provides training result and training parameters.
UC3 - Run the model - Use provides a training model, seed word and the script provides the computer-generated reviews.
UC4 - Share results with user. This notebook provides contrast on how model behaves with different datasets.
UC5 - Provide a diagnostic view of how the model learns the word corpus.

For every script, there will be a test script accompanied with it.</td>
  </tr>
  <tr>
    <td>Test Cases</td>
    <td><Gautam>
TC1 - Prepare unit test cases for each module and script developed, to ensure each performs consistently as per the requirements.
TC2 - Prepare integration test cases to ensure the application performs as intended post merging of all the individual components.
TC3 - Prepare regression test cases to ensure functionality remains unchanged, after code additions and new modifications.
TC4 - User acceptance testing, for completeness and user sign off as a final deliverable.</td>
  </tr>
  <tr>
    <td>Components</td>
    <td><Toan>
UC1: Prepare the data
C1: 
Name: download_data()
What it does: download dataset from Kaggle
Inputs: Kaggle/data-source URL
Outputs: .sql database or .csv
Technology: Kaggle API, ...

C2: 
Name: process_data()
What it does: pre-process data from a downloaded dataset
Inputs: .sql database file or .csv file
Outputs: .txt file
How use other component: C1
Technology: MySQL
UC2: Train
C1: 
Name: model()
What it does: specify the model architecture to learn the word embeddings
Inputs: .txt file
Outputs: model components
How use other component: C2

C2:
Name: train()
What it does: train the model using the predefined neural network graphs. 
Inputs: user will define model parameters including number of epoches, learning rate, batch size, etc. 
Outputs: model weights (.pt file)
Use other component: model()

UC3: Generate and evaluate performance on different datasets
C1:
Name: generate()
What it does: run the trained model on the training dataset to generate baseline results.
Inputs: model weights (.pt file)
Outputs: computer-generated review (.txt file)

C2:
Name: evaluate()
What it does: Run the trained model on different review datasets and generate results. Evaluate their qualities.
Inputs: model weights (.pt file)
Outputs: computer-generated reviews (.txt file) with different combinations of model settings and datasets.
Use other component: generate()

UC4: Generate reports and summarize our findings
C1: 
Name: iPython notebooks
What it does: generate reports and summarize our findings. State challenges, limitations, and suggestions for further improvements
Inputs: model results
Outputs: plots and .pdf report.

UC5: Diagnostics 
C1:
Name: generate_diagnostics()
What it does:provide a visual view of the model performance during training for diagnostics
Inputs: Current model parameters; train/test data
Outputs: Graph with loss function (possibly)</td>
  </tr>
</table>


<table>
  <tr>
    <td>Technology Choice</td>
    <td>https://github.com/spro/char-rnn.pytorch <Toan>
https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py <Amitabh>
https://github.com/hunkim/word-rnn-tensorflow <Gautam>

Data Sharing
Machine Learning
Data Visualization
</td>
  </tr>
  <tr>
    <td>Who are the users and what do they know</td>
    <td><Amitabh></td>
  </tr>
  <tr>
    <td>What information users want from the system</td>
    <td><Amitabh></td>
  </tr>
</table>


