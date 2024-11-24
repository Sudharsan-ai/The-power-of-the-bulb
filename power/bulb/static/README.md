# Ex.05 Design a Website for Server Side Processing
## Date:

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power Calculator</title>
    <style>
        body {
            background-color: #bdd1d3;
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
            text-align: center;
            font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            color: #006064;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        .container {
            background-color: #c9c4b7;
            border-radius: 12000px;
            padding: 20px;
            box-shadow:#f71bdd;
            display:inline-block;
            margin-top: 100px;
        }
        label {
            font-size: 100%;
            display:flow-root;
            margin: 15px 0 5px;
        }
        input[type="number"] {
            width: calc(75% - 24px);
            padding: 10px;
            border-radius: 12px;
            border: 1px solid #051313;
            margin-bottom: 15px;
            font-size: 1em;
        }
        button {
            background-color: #1fe374;
            color: rgb(211, 241, 247);
            border: none;
            border-radius: 10px;
            padding: 10px 21px;
            font-size: 1em;
            cursor:pointer;
        }
        button:hover {
            background-color: #d588b2;
        }
        p {
            font-size: 1.2em;
            margin-top: 20px;
        }
    </style>
    <script>
        function calculate() {
            const Intesity = parseFloat(document.getElementById('t1').value);
            const Resistance = parseFloat(document.getElementById('t2').value);
           
            if (isNaN(Intesity) || isNaN(Resistance)) {
                alert("Please enter valid numbers.");
                return;
            }

            const Power = (Intesity * Intesity ) * Resistance;
            document.getElementById('t3').innerText = "The power of the bulb: " + Power + " watts";
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>The Power of the Bulb</h1>
        <label for="t1">Intensity (A):</label>
        <input type="number" id="t1" placeholder="Enter the Intensity value">
        
        <label for="t2">Resistance (Ohm):</label>
        <input type="number" id="t2" placeholder="Enter the Resistance value">
        
        <button onclick="calculate()">Calculate</button>
        <p id="t3"></p>
    </div>
</body>
</html>

```


## SERVER SIDE PROCESSING:


## HOMEPAGE:


## RESULT:
The program for performing server side processing is completed successfully.