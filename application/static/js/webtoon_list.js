function draw_star() {
        $('.rating').raty({
                path: raty_img,
                score: function() {
                        return $(this).attr('toon-score');
                },
                click: function(score, evt) {
                        console.log(score);
                        console.log($(this).attr('toon-id'));
                        post_webtoon_score($(this).attr('user-id'), $(this).attr('toon-id'), score, $(this).attr('toon-title'));
                }
        });
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

function post_webtoon_score(id, webtoon, score, title) {
        $.ajax({
                url: '/evaluate_webtoon',
                type: 'POST',
                data: {"id": id, "webtoon": webtoon, "score": score},
                success:function(resp) {
                        console.log(resp);
                        noty({
                                text: title + '에 ' + score.toString() + "점을 주셨습니다",
                                type: 'information',
                                timeout: '2000',
                                animation: {
                                        open: 'animated fadeIn', // Animate.css class names
                                        close: 'animated fadeOut', // Animate.css class names
                                }
                        });
                },
                error: function() {
                        console.log("error");
                },
                complete: function() {
                        console.log("complete");
                }
        });
}
