$(function() {
  $('#calculate').click(function(){
    $.ajax({
      url: '/addnumber',
      data:{
        a: $('#a').val(),
        b: $('#b').val(),
        access_code: 'rwd'
      },
      dataType: 'JSON',
      type: 'GET',
      success: function(data){
          $("#result").html(data.result);
      }
      });
   });
});
