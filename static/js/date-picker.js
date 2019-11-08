// Updates the URL query string when a new date is selected and refreshes the page
function NewDate(key, value)
{
	window.location.href = UpdateQueryString(key, value)
}

// Create a new URL query string with updated keys and values
function UpdateQueryString(key, value, url)
{
	if (!url) url = window.location.href;
	var re = new RegExp("([?&])" + key + "=.*?(&|#|$)(.*)", "gi"),
		hash;

	if (re.test(url))
	{
		if (typeof value !== 'undefined' && value !== null)
		{
			return url.replace(re, '$1' + key + "=" + value + '$2$3');
		} 
		else
		{
			hash = url.split('#');
			url = hash[0].replace(re, '$1$3').replace(/(&|\?)$/, '');
			if (typeof hash[1] !== 'undefined' && hash[1] !== null)
			{
					url += '#' + hash[1];
			}
			return url;
		}
	}
	else {
		if (typeof value !== 'undefined' && value !== null)
		{
			var separator = url.indexOf('?') !== -1 ? '&' : '?';
			hash = url.split('#');
			url = hash[0] + separator + key + '=' + value;
			if (typeof hash[1] !== 'undefined' && hash[1] !== null)
			{
					url += '#' + hash[1];
			}
			return url;
		}
		else
		{
			return url;
		}
	}
}