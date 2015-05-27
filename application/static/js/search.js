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
	get_webtoons_by_title(title, author, is_finished);
}

function get_webtoons_by_title(title, author, is_finished) {
	$.ajax({
	    url: '/get_webtoons_by_title',
	    type:'POST',
	    data: {"title": title,
	           "author": author,
	           "is_finished": is_finished},
	    success:function(response){
			$('#result').replaceWith(response);
			$('.rating').raty({
	                	path: raty_img,
				click: function(score, evt) {
					console.log(score);
					console.log($(this).attr('toon-id'));
					post_webtoon_score($(this).attr('user-id'), $(this).attr('toon-id'), score);
				}
	        	});

	    },
	    error: function(){
	      	console.log("error");
	    },
	    complete:function(){
	      	console.log('complete');
           }
  	});
}

function post_webtoon_score(id, webtoon, score) {
	$.ajax({
		url: '/evaluate_webtoon',
		type: 'POST',
		data: {"id": id, "webtoon": webtoon, "score": score},
		success:function(resp) {
			console.log(resp);
		},
		error: function() {
			console.log("error");
		},
		complete: function() {
			console.log("complete");
		}
	});
}
