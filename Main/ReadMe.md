# Behaviour Simulation Challenge

## Description

### Behaviour Simulation
Given the content of a tweet (text, company, username, media URLs, timestamp), the
task is to predict its user engagement, measured by likes.
### Content Simulation
Given the tweet metadata (company, username, media URL, timestamp), generate
the tweet text.

## Approch
### Task 1 : Behaviour Simulation

<p align="center">
    <img src = "media\Task1.jpg" height="300" alt="Image">
  <br>
  <em>Approach for Task 1</em>
</p>

Our approach for behaviour simulation starts by dividing the inputs into four categories :-
- Company
- Image
- Tweet Content
- Tweet Metadata like sentiment,date,time,mention_count,hyperlink_count and so on.

1. For the company we have have embedded the company name using Word2Vec
2. For the image and the tweet content we have used CLIP to get 768 dimnesional embedding for each. These are processed through a dense layer.
3. For the meta-deta we have a 13 dimensional array.

These three are than concatenated and given as input to a series of dense layers that give the final likes as output.

### Task 2 : Content Simulation

<p align="center">
    <img src = "media\Task2.jpg" height="300" alt="Image">
  <br>
  <em>Approach for Task 2</em>
</p>

For the content simulation task, we have followed the underlying procedure :-
1. For the tweet media we have used captioning models
2. Then using these captions and the tweet meta deta we have engineered a prompt and then given it LLM for tweet generation

After experimenting with various models we decided to go with fastdup-blip model for captions and open-ai gpt-3.5-turbo for the tweet generation.

<!-- ![Approach for Task 1](media\Task1.jpg)
![Approach for Task 2](media\Task2.jpg) -->

## Contents
This repository contains the following :-
1. Colab Notebooks for both the tasks. Instructions for which is mentioned in the notebook itself. 
2. [result](result/) folder containing result :-
    - [behaviour_simulation_test_company.xlsx](/results/behaviour_simulation_test_company.xlsx)
    - [behaviour_simulation_test_time.xlsx](/results/behaviour_simulation_test_time.xlsx)
    - [content_simulation_test_company.xlsx](/results/content_simulation_test_company.xlsx)
    - [content_simulation_test_time.xlsx](/results/content_simulation_test_time.xlsx)
3. Report for the problem statement. 
4. [Experiments](Experiments/) folder, containing notebooks for all the approaches undertaken by us.
5. [Task_1](Task_1/) folder, containing the code for running our Behaviour Simulation model on custom dataset.
6. [Task_2](Task_2/) folder, containing the code for running our Content Simulation model on custom dataset.

## Instructions
For the instructions on how to run the models, check out the ReadMe in the [Task_1](Task_1/) and [Task_2](Task_2/) folder.If for any reason the code does not run, please go to the colab instances :-
- [Colab instance for task 1](https://colab.research.google.com/drive/15yXlPs_nXZrbGHF64Tn_Klmpk5oQWxoF?usp=sharing)
- [Colab instance for task 2](https://colab.research.google.com/drive/1Lyfixl-h7PeEf8RakbjMA9LWdhfl2mBe?usp=sharing)