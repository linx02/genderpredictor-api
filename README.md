# genderpredictor-api

API endpoint: https://gender-predictor-api-43d1edacb61c.herokuapp.com/predict

To use the Gender Prediction API, you can send a POST request containing an image file to the provided endpoint.
The API will process the image and return a prediction of the gender ('male' or 'female') in JSON format.
Below are the steps to interact with the API:

## Usage

* Send a POST request to the endpoint with an image file using the multipart/form-data content type.

__Example using cURL:__

```bash
curl -X POST -F "file=@path/to/your/image.jpg" https://gender-predictor-api-43d1edacb61c.herokuapp.com/predict
```

* Upon successful processing of the image, the API will respond with a JSON object containing the predicted gender.
* The response will include a 'gender' key with a value of either 'male' or 'female'.

__Example response:__

```json
{
    "gender": "female"
}
```
