import os
import click
import pandas as pd
from pycaret.classification import predict_model, load_model


# OPTIONAL: create a class in your Python module to hold the functions that you created
class ChurnPredictor:
    def load_data(filepath):
        """
        Loads data into a DataFrame from a string filepath
        """
        df = pd.read_csv(filepath, index_col='customerID')

        return df


    def make_predictions(dataframe):
        """
        Uses the pycaret best model to make predictions on data in the df dataframe
        """
        model = load_model('LR')
        predictions = predict_model(model, data=dataframe)
        predictions.rename({'Label': 'Churn_prediction'}, axis=1, inplace=True)
        predictions['Churn_prediction'].replace({1: 'Churn', 0: 'No churn'},
                                                inplace=True)
        
        return predictions['Churn_prediction']


# OPTIONAL: accept user input to specify a file using a tool such as
#           i) Python's input() function, 
#           ii) the ***click*** package for command-line arguments, or
#           iii) GUI
@click.command()
@click.option("--filename", 
              prompt="Enter the full path to a CSV file", 
              help="ex. data\\new_churn_data.csv",
              default='data\\new_churn_data.csv')
def prompt_for_file(filename):
    try:
        if os.path.exists(filename):
            df = ChurnPredictor.load_data(filename)    # ('data/new_churn_data.csv')
            predictions = ChurnPredictor.make_predictions(df)
            print('Predictions:\n{}'.format(predictions))
        else:
            print('Unable to locate file {}'.format(str(filename)))
    except Exception as error:
        print('Error occured: {}'.format(str(error)))


if __name__ == "__main__":
    # prompt for filename
    # bool_return = prompt_for_file()

    df = ChurnPredictor.load_data('data/new_churn_data.csv')
    predictions = ChurnPredictor.make_predictions(df)
    print('predictions:')
    print(predictions)