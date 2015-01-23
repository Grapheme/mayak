$(function() {
	
	function getWindDir(dir){
		var directionsEn2Ru = {
			N: 'северный',
			NNE: 'северо-восточный',
			NE: 'северо-восточный',
			ENE: 'северо-восточный',
			E: 'восточный',
			ESE: 'юго-восточный',
			SE: 'юго-восточный',
			SSE: 'юго-восточный',
			S: 'южный',
			SSW: 'юго-западный',
			SW: 'юго-западный',
			WSW: 'юго-западный',
			W: 'западный',
			WNW: 'северо-западный',
			NW: 'северо-западный',
			NNW: 'северо-западный',
		};
		
		return directionsEn2Ru[dir];
	};
	
	function getCurWeather(code) {
		var weatherArr = [
			'Торнадо',
			'Тропический шторм',
			'Ураган',
			'Сильные грозы',
			'Грозы',
			'Снег с дождем',
			'Мокрый снег',
			'Мокрый снег',
			'Изморозь',
			'Дождь',
			'Ледяной дождь',
			'Ливень',
			'Ливень',
			'Снегопад',
			'Снегопад',
			'Метели',
			'Снег',
			'Град',
			'Мокрый снег',
			'Пыльно',
			'Туман',
			'Дымка',
			'Дымка',
			'Ветрено',
			'Ветрено',
			'Холодно',
			'Облачно',
			'Облачно (ночь)',
			'Облачно (день)',
			'Переменная облачность (ночь)',
			'Переменная облачность (день)',
			'Ясно (ночь)',
			'Солнечно',
			'Ясно (ночь)',
			'Ясно (день)',
			'Дождь с градом',
			'Жара',
			'Местами грозы',
			'Местами грозы',
			'Местами грозы',
			'Дождь',
			'Сильный снег',
			'Сильный снегопад',
			'Сильный снегопад',
			'Переменная облачность',
			'Ливни с грозой',
			'Снегопад',
			'Местами дождь'
		];
		if(weatherArr[code]) {
			return weatherArr[code];
		}
		else return 'переменная облачность';
	}
		
	$.simpleWeather({
		zipcode: '',
		woeid: '2123177',
		location: '',
		unit: 'c',
		speed: 'kph',
		success: function(weather) {
			/*html = '<p><img src="'+weather.thumbnail+'"></p>';
			html += '<a class="weather-header" href="http://rp5.ru/Погода_в_Даховской" target="_blank">Сегодня в Даховской:</a>';
			html += '<div class="weather-columns clearfix"><div class="weather-temp"><span class="italic-capt">Температура</span> '+weather.high+'...'+weather.low+'&deg;</div>';			
			html += '<div class="weather-wind"><span class="italic-capt">Ветер </span>'+getWindDir(weather.wind.direction)+' '+Math.round(weather.wind.speed * 1000 / 3600 * 100) / 100+' м/с</div>';
			html += '<div class="current-weather"><span class="italic-capt">'+ getCurWeather(weather.code) +' </span></div>';
			*/
			console.log(weather);
			var widget = $('.widget .weather');
			widget.find('.visual').attr('src', weather.thumbnail);
			widget.find('.temp').text(weather.high+'...'+weather.low);
		},
		error: function(error) {
			console.log(error)
			//$("#weather").html('<p>'+error+'</p>');
		}
	});
});