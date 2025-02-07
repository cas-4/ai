# CAS4 ai

<img src="https://avatars.githubusercontent.com/u/175958109?s=100&v=4" alt="Logo" align="right"/>

This repo refers to an AI study for the project of
[Context Aware System](https://www.unibo.it/en/study/phd-professional-masters-specialisation-schools-and-other-programmes/course-unit-catalogue/course-unit/2023/479036)
class at the [University of Bologna](https://unibo.it).

## Activity Recognition Model

This project uses a Random Forest Classifier to predict user activities based on the speed of movement, time of day, and day of the week. The model is trained on a dataset containing the speed, timestamp, and supposed activity of users. This model can be used to recognize whether a user is still, walking, running, or in a vehicle.
Features

The model can predict user activity using two approaches:

* With only speed: The activity prediction is based solely on the speed of movement.

* With speed, hour of day, and day of week: The model also considers the time of day and the day of the week, which can provide additional context and improve accuracy, especially when recognizing habits, such as weekend behavior.

### With Only Speed Parameter

In this case, the model is trained using only the speed of movement to predict activity. Here's an example of the output:

```
Classification Report:
              precision    recall  f1-score   support

           0       0.86      1.00      0.92        12
           1       0.81      0.84      0.82        64
           2       0.69      0.80      0.74        55
           3       0.99      0.83      0.90        87

    accuracy                           0.83       218
   macro avg       0.83      0.87      0.85       218
weighted avg       0.85      0.83      0.84       218

Add speed: 4.2
Predicted activity for speed 4.2 m/s: WALKING
```

### With Speed, Hour of Day, and Day of Week Parameters

In this case, the model uses speed, hour of the day, and day of the week. This approach takes into account user habits depending on the time of day and the day of the week. This can improve activity recognition, especially on weekends.

```
Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        12
           1       0.94      0.78      0.85        64
           2       0.76      0.93      0.84        55
           3       0.97      0.95      0.96        87

    accuracy                           0.90       218
   macro avg       0.92      0.92      0.91       218
weighted avg       0.91      0.90      0.90       218

Add speed: 4.2
Add hour of the day: 8
Add day of the week: 6
Predicted activity for speed 4.2 m/s: RUNNING
```

## Why?

While Android and iOS both provide activity recognition APIs, this model is used in a React Native application that operates independently of the native Android and iOS activity recognition features. Therefore, it provides a custom solution tailored for cross-platform development.

The model considers user behavior patterns such as time of day and day of the week, allowing it to better recognize activities by accounting for changes in user habits, especially on weekends.

## How to use

We used [uv](https://astral.sh/uv). After the environment creation you need to:

1. Load the dataset (e.g., user_activity.csv) containing the speed, timestamp, and supposed activity of users.
2. Train the Random Forest Classifier with the features of your choice (either just speed or additional parameters like hour of day and day of week).
3. Predict user activity by inputting the current speed, and optionally, hour of the day and day of the week.
