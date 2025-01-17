<?php
// Retrieve and sanitize the form data
$cardNumber = $_POST['cardNumber'];
$nickname = $_POST['nickname'];
$expiryDate = $_POST['expiryDate'];
$cvc = $_POST['cvc'];
$RP ="250";

// Sanitize and validate data (not shown in this example - but highly recommended)

// Establish connection to your MySQL database
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "League";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Insert data into your database
$sql = "INSERT INTO card_details (card_number, nickname, expiry_date, cvc,RP)
        VALUES ('$cardNumber', '$nickname', '$expiryDate', '$cvc','$RP')";


if ($conn->query($sql) === TRUE) {
    header("Location: index.html"); // Redirect to index.html on success
    exit(); // Ensure that no further code is executed after the redirect
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}




$conn->close();
?>
