$('#file-upload').change(function() {
  var i = $(this).prev('label').clone();
  var file = $('#file-upload')[0].files[0].name;
  $(this).prev('label').text(file);
});

var imageChanged = function(input, event) {
    console.log(event)
    if(event.target.files.length > 0){
        var filename = event.target.files[0].name;
        $('#file_selected').html(filename);
    }
    else {
        $('#file_selected').html("")
    }
}
