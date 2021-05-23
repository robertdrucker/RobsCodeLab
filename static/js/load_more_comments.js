$(function() {
  const pathname = window.location.pathname;
  /*
    remove leading '/posts/' from pathname 
    Example: posts/21-understanding-tags-field becomes
    21-understanding-tags-field
  */
  const slug = pathname.replace('/posts/','');

  $(".comments__reset").click(function () {
    $.ajax({
      url: '/clear_comments_count',
      success: function(data){
        max_initial_comments = data.result['max_initial_comments']

        $("#comments-load-options").removeClass('comments__load');
        $("#comments-load-options").addClass('comments__loading');
        $(".comments__loading").text("Resetting...");
        $("#comments-reset").addClass('comments__reset--hide');
      
        setTimeout(function (max_init_comments) {
          // Remove specified number of comments
          $(".comment:nth-child(" + max_init_comments + ")").nextAll(".comment").remove().fadeIn("slow");
        
          $("#comments-load-options").addClass('comments__load');
          $("#comments-load-options").removeClass('comments__loading');
        
          $("#comments-load-options").removeClass('comments__load--hide');
          $("#comments-reset").addClass('comments__reset--hide');
          $("#comments-load").addClass('comments__load');
          $(".comments__load").text("See more");
        }, 1000, max_initial_comments);
      }     
    });
  })

  $('#comments-load-options').click({slug: slug}, function(){
    $.ajax({
      url: '/load_more_comments/'+slug,
      data:{
        access_code: 'rwd'
      },
      type: 'GET',
      beforeSend: function () {
        $("#comments-load-options").removeClass('comments__load');
        $("#comments-load-options").addClass('comments__loading');
        $(".comments__loading").text("Loading...");
        $("#comments-reset").addClass('comments__reset--hide');
      },
      success: function(data){
        setTimeout(function() {

          $("#comments-reset").removeClass('comments__reset--hide');
          $("#comments-load-options").removeClass('comments__loading');
          $("#comments-load-options").addClass('comments__load');

          comments = data.result['comment_html_list']
          more_comments_btn_display = data.result['more_comments_btn_display']

          result_html = ''
          $.each( comments, function(index){
            result_html += comments[index]
          });
          if (!more_comments_btn_display) {
            $("#comments-load-options").addClass("comment__more-comments-button--hide")
          }
          $("#result").append(result_html)

          // checking row value is greater than allcount or not
          if (!more_comments_btn_display) {
            // Change the text and background
            $("#comments-load-options").addClass('comments__load--hide');
          } else {
            $(".comments__load").text("See more");
          }
        }, 1000)
      }   
    });
   });
});
