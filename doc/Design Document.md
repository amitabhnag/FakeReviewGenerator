# Fake Review Generator

## Design Document

<img src="/doc/FakeReviewGeneratorArchitecture.jpg" width="800">

<table>
  <tr>
    <td>Topic</td>
    <td>Details </td>
  </tr>
  <tr>
    <td>Top Question</td>
    <td>How to simulate text generation by learning from a dataset of user reviews on Amazon and a music discussion site? <br>
</td>
  </tr>
  <tr>
    <td>Use Cases</td>
    <td>
UC1 - Prepare the data and make sure it is compatible with the training pipeline.<br>
UC2 - Train the model. User provides a dataset and the script provides training result and training parameters.<br>
UC3 - Run the model - Use provides a training model, seed word and the script provides the computer-generated reviews.<br>
UC4 - Share results with user. This notebook provides contrast on how model behaves with different datasets.<br>
UC5 - Provide a diagnostic view of how the model learns the word corpus.<br>

For every script, there will be a test script accompanied with it.</td>
  </tr>
  <tr>
    <td>Test Cases</td>
    <td>
TC1 - Prepare unit test cases for each module and script developed, to ensure each performs consistently as per the requirements. <br>
TC2 - Prepare integration test cases to ensure the application performs as intended post merging of all the individual components. <br>
TC3 - Prepare regression test cases to ensure functionality remains unchanged, after code additions and new modifications.<br>
TC4 - User acceptance testing, for completeness and user sign off as a final deliverable.</td> <br>
  </tr>
  <tr>
    <td>Components</td>
    <td>
UC1: Prepare the data <br>
C1: <br>
Name: download_data() <br>
What it does: download dataset from Kaggle <br>
Inputs: Kaggle/data-source URL <br>
Outputs: .sql database or .csv <br>
Technology: Kaggle API, ... <br>

C2: <br>
Name: process_data() <br>
What it does: pre-process data from a downloaded dataset <br>
Inputs: .sql database file or .csv file <br>
Outputs: .txt file <br>
How use other component: C1 <br>
Technology: MySQL <br>
UC2: Train <br>
C1: <br>
Name: model() <br>
What it does: specify the model architecture to learn the word embeddings <br>
Inputs: .txt file <br>
Outputs: model components <br>
How use other component: C2 <br>

C2: <br>
Name: train() <br>
What it does: train the model using the predefined neural network graphs. <br>
Inputs: user will define model parameters including number of epoches, learning rate, batch size, etc. <br>
Outputs: model weights (.pt file) <br>
Use other component: model() <br>

UC3: Generate and evaluate performance on different datasets <br>
C1: <br>
Name: generate() <br>
What it does: run the trained model on the training dataset to generate baseline results. <br>
Inputs: model weights (.pt file) <br>
Outputs: computer-generated review (.txt file) <br>

C2: <br>
Name: evaluate() <br>
What it does: Run the trained model on different review datasets and generate results. Evaluate their qualities.<br>
Inputs: model weights (.pt file) <br>
Outputs: computer-generated reviews (.txt file) with different combinations of model settings and datasets. <br>
Use other component: generate() <br>

UC4: Generate reports and summarize our findings <br>
C1: <br>
Name: iPython notebooks <br>
What it does: generate reports and summarize our findings. State challenges, limitations, and suggestions for further improvements <br>
Inputs: model results <br>
Outputs: plots and .pdf report. <br>

UC5: Diagnostics  <br>
C1: <br>
Name: generate_diagnostics() <br>
What it does:provide a visual view of the model performance during training for diagnostics <br>
Inputs: Current model parameters; train/test data <br>
Outputs: Graph with loss function (possibly)</td> <br>
  </tr>
</table>


<table>
  <tr>
    <td>Technology Choice</td>
    <td>
      In progress<br>
      https://github.com/spro/char-rnn.pytorch <br>
https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py <br>
https://github.com/hunkim/word-rnn-tensorflow <br>

Data Sharing <br>
Machine Learning <br>
Data Visualization <br>
</td>
  </tr>
  <tr>
    <td>Who are the users and what do they know</td>
    <td>In progress</td>
  </tr>
  <tr>
    <td>What information users want from the system</td>
    <td>In progress</td>
  </tr>
</table>


