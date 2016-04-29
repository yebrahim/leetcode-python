class Solution(object):
	def reverseVowels(self, str):
		vowels2 = list(zip(*[(a,b) for a,b in enumerate(str) if b in ['a','e','o','u','i','A','E','O','U','I']]))
		rvowels = dict(zip(vowels2[0], vowels2[1][::-1])) if len(vowels2) else {}
		return (''.join(list(map(lambda x : x[1] if x[0] not in rvowels else rvowels[x[0]], enumerate(str)))))

        