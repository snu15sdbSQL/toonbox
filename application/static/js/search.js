$(document).ready(function(){

	$("#search_btn").click(function() {
		var title = $("#search_input").val();
		get_webtoons_by_title(title);
	});
	

});

function get_webtoons_by_title(title) {
	$.ajax({
	    url: '/get_webtoons_by_title',
	    type:'POST',
	    data: {"title": title},
	    success:function(response){
		    console.log(response); 
			$('#result').replaceWith(response);
	    },
	    error: function(){
	      	console.log("error");
	    },
	    complete:function(){
	      	console.log('complete');
	    }
    
  	});
}
