<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <!-- Bootstrap core CSS -->
    <link href="public/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="public/css/main.css?v=<?= time(); ?>" rel="stylesheet">
    <link rel="stylesheet" href="public/vendor/toastr/css/toastr.min.css">
    <!-- Bootstrap core JavaScript -->
    <script src="public/vendor/jquery/jquery.min.js"></script>
    <script src="public/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
    <script src="public/js/script.js?v=<?= time(); ?>"></script>
    <script src="public/vendor/toastr/js/toastr.min.js"></script>
    <title>Patient Record</title>
</head>

<body>
    <div class="container py-5">
        <!-- For demo purpose -->
        <header class="text-white text-center">
            <h1 class="display-4">Patient Photo</h1>
        </header>

        <div class="row">
            <div class="col-lg-6 mx-auto">
                <!-- Upload image input-->
                <div class="input-group mb-3 px-2 py-2 rounded-pill bg-white shadow-sm">
                    <input id="upload" type="file" accept=".jpg, .jpeg, .png" class="form-control border-0">
                    <label id="upload-label" for="upload" class="font-weight-light text-muted">
                        Choose file
                    </label>
                    <div class="input-group-append">
                        <label for="upload" class="btn btn-light m-0 rounded-pill px-4">
                            <i class="fa fa-cloud-upload mr-2 text-muted"></i>
                            <small class="text-uppercase font-weight-bold text-muted">Choose file</small>
                        </label>
                    </div>
                </div>
            </div>
        </div>

        <header class="text-white text-center">
            <h1 class="display-4">Patient Record</h1>
        </header>

        <div class="container">
            <form action="/action_page.php" class="col-lg-8 mx-auto text-white">
            <div class="row">
                <div class="col-25">
                    <label for="fname">First Name</label>
                </div>
                <div class="col-75">
                    <input type="text" id="fname" name="firstname" placeholder="First name..">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="lname">Last Name</label>
                </div>
                <div class="col-75">
                    <input type="text" id="lname" name="lastname" placeholder="Last name..">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="nin">National ID Number</label>
                </div>
                <div class="col-75">
                    <input type="text" id="nin" name="nin" placeholder="National ID Number..">
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="province">Province</label>
                </div>
                <div class="col-75">
                    <select id="province" name="province">
                        <option value="hanoi">Hà Nội</option>
                        <option value="hochiminhcity">Thành phố Hồ Chí Minh</option>
                        <option value="haiphong">Hải Phòng</option>
                    </select>
                </div>
            </div>
            <div class="row">
                <div class="col-25">
                    <label for="discription">Description</label>
                </div>
                <div class="col-75">
                    <textarea id="discription" name="discription" placeholder="Write something.." style="height:200px"></textarea>
                </div>
            </div>
            </form>
        </div>

        <div class="row py-4">
            <div class="col-lg-6 mx-auto text-center">
                <button type="button" class="btn btn-primary" id="btn_submit">Submit</button>
            </div>
        </div>

        <div class="row" id="result-area" name="#">
            <?php for ($i = 0; $i < 4; $i++): ?>
                <div class="col">
                    <div class="image-area mt-4">
                        <img id="detectionResult<?= $i; ?>" src="#" alt="" class="img-fluid rounded shadow-sm mx-auto d-block">
                    </div>
                </div>
            <?php endfor; ?>
        </div>
        <div class="row">
            <div class="col-lg-6 mx-auto text-center">
                <div class="image-area mt-4">
                    <img id="detectionResult" />
                </div>
            </div>    
        </div>
    </div>
</body>
</html>
<!-- doc input va show duong dan len phan upload -->
<script>
/*  ==========================================
    SHOW UPLOADED IMAGE
    ========================================== */
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#imageResult')
                .attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    $(function () {
        $('#upload').on('change', function () {
            readURL(input);
        });
    });

/*  ==========================================
    SHOW UPLOADED IMAGE NAME
    ========================================== */
    var input = document.getElementById( 'upload' );
    var imageinfo = document.getElementById( 'upload-label' );
    input.addEventListener( 'change', showFileName );
    function showFileName( event ) {
        var input = event.srcElement;
        var fileName = input.files[0].name;
        imageinfo.textContent = 'File name: ' + fileName;
    }
</script>
