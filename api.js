<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Interaction with JavaScript</title>
    <script>
        const baseURL = 'http://localhost:8080/api/data';

        // Function to handle GET request
        function getData() {
            fetch(baseURL)
                .then(response => response.json())
                .then(data => {
                    console.log("GET response:", data);
                    document.getElementById('response').innerText = JSON.stringify(data, null, 2);
                })
                .catch(error => console.error('Error with GET request:', error));
        }

        // Function to handle POST request
        function postData() {
            const data = {
                name: "John",
                age: 30
            };

            fetch(baseURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(response => response.json())
                .then(data => {
                    console.log("POST response:", data);
                    document.getElementById('response').innerText = JSON.stringify(data, null, 2);
                })
                .catch(error => console.error('Error with POST request:', error));
        }

        // Function to handle PUT request
        function putData() {
            const data = {
                updated: "true"
            };

            fetch(baseURL, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(response => response.json())
                .then(data => {
                    console.log("PUT response:", data);
                    document.getElementById('response').innerText = JSON.stringify(data, null, 2);
                })
                .catch(error => console.error('Error with PUT request:', error));
        }

        // Function to handle DELETE request
        function deleteData() {
            fetch(baseURL, {
                method: 'DELETE'
            })
                .then(response => response.json())
                .then(data => {
                    console.log("DELETE response:", data);
                    document.getElementById('response').innerText = JSON.stringify(data, null, 2);
                })
                .catch(error => console.error('Error with DELETE request:', error));
        }
    </script>
</head>
<body>
    <h1>API Interaction with JavaScript</h1>
    
    <button onclick="getData()">GET Data</button>
    <button onclick="postData()">POST Data</button>
    <button onclick="putData()">PUT Data</button>
    <button onclick="deleteData()">DELETE Data</button>
    
    <pre id="response"></pre>
</body>
</html>
