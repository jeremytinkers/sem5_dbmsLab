<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>findDonorResults</title>
</head>

<body>
    <?php
    include 'config.php';

    $servername = "localhost";
    $username = "root";
    $password = $adminPassword;
    $database = "lab7_db";

    $u_donor_bloodgroup = $_POST["donor_bloodgroup"];

    // Create connection
    $conn = mysqli_connect($servername, $username, $password, $database);

    // Check connection
    if (!$conn) {
        die("Connection to MySQL failed: " . mysqli_connect_error());
    }

    $sql = "SELECT donor_name, donor_id, donor_aadharNo FROM Donors where donor_bloodgroup = '$u_donor_bloodgroup' ";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "<table><tr><th>ID</th><th>Name</th><th>Aadhar No</th></tr>";
        // output data of each row
        while ($row = $result->fetch_assoc()) {
            echo "<tr><td>" . $row["donor_id"] . "</td><td>" . $row["donor_name"] . "</td><td>" . $row["donor_aadharNo"] . "</td></tr>";
        }
        echo "</table>";
    } else {
        echo "<div>0 results</div>";
    }
    $conn->close();
    ?>
</body>

</html>