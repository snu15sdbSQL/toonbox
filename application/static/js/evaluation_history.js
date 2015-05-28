$(document).ready(function() {
	$('.rating').raty({
		path: raty_img,
		score: function() {
			return $(this).attr('toon-score');
		},
		click: function(score, evt) {
			console.log(score);
			console.log($(this).attr('toon-id'));			
			post_webtoon_score($(this).attr('user-id'), $(this).attr('toon-id'), score);
		}
	});
});

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
