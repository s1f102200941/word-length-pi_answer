def get_pi_digits():
    text = "How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."
    cleaned_text = text.replace(",", "").replace(".", "")
    word_list = cleaned_text.split()
    numbers=list(map(len, word_list))
    result = int(''.join(map(str, numbers)))
    return result
