$(document).ready(function () {
  $('.select-option .option').click(function () {
    $('.select-option .option').each(function () {
      const $this = $(this)
      if ($this.hasClass('active')) {
        $this.removeClass('active')
      }
    })

    $(this).addClass('active')
  })

  $('#btn_submit').on('click', function () {
    const file = document.getElementById('upload').files[0];
    const message = document.getElementById('nin').value;
    console.log(message)
    if (typeof file === 'undefined') {
      toastr["warning"]("Must choose file input", "");
      return false
    }
    if (typeof message === 'undefined') {
      toastr["warning"]("Must enter national ID number", "");
      return false
    }

    const formData = new FormData();
    
    formData.append('file', file);
    formData.append('message', message);
    formData.append('action', 'upload-file');

    // toastr for report successful submit
    toastr.options = {
      "closeButton": false,
      "debug": false,
      "newestOnTop": false,
      "progressBar": false,
      "positionClass": "toast-top-center",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "2000",
      "hideDuration": "2000",
      "timeOut": "10000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
    }

    toastr["warning"]("Pending result...", "")


    $.ajax({
      type: 'POST',
      dataType: 'json',
      cache: false,
      data: formData,
      url: 'handle.php',
      processData: false,
      contentType: false,
      success: function (data) {
        if (data.code && data.code === 200) {
          var src = data.src.split("\n");
          var len = src.length
          console.log(`${len}: ${src}`)
          $('#result-area').attr('name', len)
          for (const i in src) {
            if (i < len - 2) {
              $('#detectionResult' + i).attr('src', src[i])
            }
          }
          $('#detectionResult').attr('src', src[len - 2])
          toastr["success"](data.time + " seconds", "Successfully!")
        } else {
          toastr["error"](data.message, "Error!")
        }
      },
      error: function (e) {
        console.log("Error", e)
      }
    });


  })

});
