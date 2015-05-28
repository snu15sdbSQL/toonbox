$(document).ready(function(){

	$("#search_btn").click(function() {
		search_handler();
	});
	$(document).keypress(function(e) {
    		if(e.which == 13) search_handler();
    	});
});
	
function search_handler() {
	var title = $("#search_input").val(); //string
	var author = $("#author_input").val(); //string
	var is_finished = $("#finished_input").is(":checked").toString();  //string
	get_webtoons_by_title(title, author, is_finished, user_id);
}

function get_webtoons_by_title(title, author, is_finished, user_id) {
        $.ajax({
            url: '/get_webtoons_by_title',
            type:'POST',
            data: {"title": title,
                   "author": author,
                   "is_finished": is_finished,
		   "user_id": user_id},
            success:function(response){
                        $('#result').replaceWith(response);
                        draw_star();
            },
            error: function(){
                console.log("error");
            },
            complete:function(){
                console.log('complete');
           }
        });
}
