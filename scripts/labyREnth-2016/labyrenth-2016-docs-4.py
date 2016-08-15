#!/usr/bin/env python

target = 'BZb+NKtmD9XQ6uQAgJsuvvudb7tZgoD/RCJX'[::-1].decode('base64')
str2 = 'xRgWTqWr7ipEjFBfESrOiaYFu9i9Jml3Q171'.decode('base64')

def brute_flag():
	s06 = ''
	for i in range(len(str2)):
		s06 += chr( ord( target[i] ) ^ ord( str2[i] ) )
	print s06

	t2 = ''
	for i in range(len(s06)):
		t2 += chr( ord(s06[i]) ^ 54 )
	print t2

	t1 = ''
	for i in range(len(t2)):
		t1 += chr( ord(t2[i]) ^ 255)
	print t1

brute_flag()


'''
flag: PAN{VBA=V3ryb!gAdv3n7ur3s!}

all of the following values work as width and zoom
>>> p = 'P'
>>> for x in range(0x100):
...     t1 = ord(p) ^ x
...     for y in range(0x100):
...             t2 = t1 ^ y
...             if (t2 ^ 0xc5) == 0x5c:
...                     print "width: " + str(x)
...                     print "zoom : " + str(y)
...                     print
...
width: 0
zoom : 201

width: 1
zoom : 200

width: 2
zoom : 203

width: 3
zoom : 202

width: 4
zoom : 205

width: 5
zoom : 204

width: 6
zoom : 207

width: 7
zoom : 206

width: 8
zoom : 193

width: 9
zoom : 192

width: 10
zoom : 195

width: 11
zoom : 194

width: 12
zoom : 197

width: 13
zoom : 196

width: 14
zoom : 199

width: 15
zoom : 198

width: 16
zoom : 217

width: 17
zoom : 216

width: 18
zoom : 219

width: 19
zoom : 218

width: 20
zoom : 221

width: 21
zoom : 220

width: 22
zoom : 223

width: 23
zoom : 222

width: 24
zoom : 209

width: 25
zoom : 208

width: 26
zoom : 211

width: 27
zoom : 210

width: 28
zoom : 213

width: 29
zoom : 212

width: 30
zoom : 215

width: 31
zoom : 214

width: 32
zoom : 233

width: 33
zoom : 232

width: 34
zoom : 235

width: 35
zoom : 234

width: 36
zoom : 237

width: 37
zoom : 236

width: 38
zoom : 239

width: 39
zoom : 238

width: 40
zoom : 225

width: 41
zoom : 224

width: 42
zoom : 227

width: 43
zoom : 226

width: 44
zoom : 229

width: 45
zoom : 228

width: 46
zoom : 231

width: 47
zoom : 230

width: 48
zoom : 249

width: 49
zoom : 248

width: 50
zoom : 251

width: 51
zoom : 250

width: 52
zoom : 253

width: 53
zoom : 252

width: 54
zoom : 255

width: 55
zoom : 254

width: 56
zoom : 241

width: 57
zoom : 240

width: 58
zoom : 243

width: 59
zoom : 242

width: 60
zoom : 245

width: 61
zoom : 244

width: 62
zoom : 247

width: 63
zoom : 246

width: 64
zoom : 137

width: 65
zoom : 136

width: 66
zoom : 139

width: 67
zoom : 138

width: 68
zoom : 141

width: 69
zoom : 140

width: 70
zoom : 143

width: 71
zoom : 142

width: 72
zoom : 129

width: 73
zoom : 128

width: 74
zoom : 131

width: 75
zoom : 130

width: 76
zoom : 133

width: 77
zoom : 132

width: 78
zoom : 135

width: 79
zoom : 134

width: 80
zoom : 153

width: 81
zoom : 152

width: 82
zoom : 155

width: 83
zoom : 154

width: 84
zoom : 157

width: 85
zoom : 156

width: 86
zoom : 159

width: 87
zoom : 158

width: 88
zoom : 145

width: 89
zoom : 144

width: 90
zoom : 147

width: 91
zoom : 146

width: 92
zoom : 149

width: 93
zoom : 148

width: 94
zoom : 151

width: 95
zoom : 150

width: 96
zoom : 169

width: 97
zoom : 168

width: 98
zoom : 171

width: 99
zoom : 170

width: 100
zoom : 173

width: 101
zoom : 172

width: 102
zoom : 175

width: 103
zoom : 174

width: 104
zoom : 161

width: 105
zoom : 160

width: 106
zoom : 163

width: 107
zoom : 162

width: 108
zoom : 165

width: 109
zoom : 164

width: 110
zoom : 167

width: 111
zoom : 166

width: 112
zoom : 185

width: 113
zoom : 184

width: 114
zoom : 187

width: 115
zoom : 186

width: 116
zoom : 189

width: 117
zoom : 188

width: 118
zoom : 191

width: 119
zoom : 190

width: 120
zoom : 177

width: 121
zoom : 176

width: 122
zoom : 179

width: 123
zoom : 178

width: 124
zoom : 181

width: 125
zoom : 180

width: 126
zoom : 183

width: 127
zoom : 182

width: 128
zoom : 73

width: 129
zoom : 72

width: 130
zoom : 75

width: 131
zoom : 74

width: 132
zoom : 77

width: 133
zoom : 76

width: 134
zoom : 79

width: 135
zoom : 78

width: 136
zoom : 65

width: 137
zoom : 64

width: 138
zoom : 67

width: 139
zoom : 66

width: 140
zoom : 69

width: 141
zoom : 68

width: 142
zoom : 71

width: 143
zoom : 70

width: 144
zoom : 89

width: 145
zoom : 88

width: 146
zoom : 91

width: 147
zoom : 90

width: 148
zoom : 93

width: 149
zoom : 92

width: 150
zoom : 95

width: 151
zoom : 94

width: 152
zoom : 81

width: 153
zoom : 80

width: 154
zoom : 83

width: 155
zoom : 82

width: 156
zoom : 85

width: 157
zoom : 84

width: 158
zoom : 87

width: 159
zoom : 86

width: 160
zoom : 105

width: 161
zoom : 104

width: 162
zoom : 107

width: 163
zoom : 106

width: 164
zoom : 109

width: 165
zoom : 108

width: 166
zoom : 111

width: 167
zoom : 110

width: 168
zoom : 97

width: 169
zoom : 96

width: 170
zoom : 99

width: 171
zoom : 98

width: 172
zoom : 101

width: 173
zoom : 100

width: 174
zoom : 103

width: 175
zoom : 102

width: 176
zoom : 121

width: 177
zoom : 120

width: 178
zoom : 123

width: 179
zoom : 122

width: 180
zoom : 125

width: 181
zoom : 124

width: 182
zoom : 127

width: 183
zoom : 126

width: 184
zoom : 113

width: 185
zoom : 112

width: 186
zoom : 115

width: 187
zoom : 114

width: 188
zoom : 117

width: 189
zoom : 116

width: 190
zoom : 119

width: 191
zoom : 118

width: 192
zoom : 9

width: 193
zoom : 8

width: 194
zoom : 11

width: 195
zoom : 10

width: 196
zoom : 13

width: 197
zoom : 12

width: 198
zoom : 15

width: 199
zoom : 14

width: 200
zoom : 1

width: 201
zoom : 0

width: 202
zoom : 3

width: 203
zoom : 2

width: 204
zoom : 5

width: 205
zoom : 4

width: 206
zoom : 7

width: 207
zoom : 6

width: 208
zoom : 25

width: 209
zoom : 24

width: 210
zoom : 27

width: 211
zoom : 26

width: 212
zoom : 29

width: 213
zoom : 28

width: 214
zoom : 31

width: 215
zoom : 30

width: 216
zoom : 17

width: 217
zoom : 16

width: 218
zoom : 19

width: 219
zoom : 18

width: 220
zoom : 21

width: 221
zoom : 20

width: 222
zoom : 23

width: 223
zoom : 22

width: 224
zoom : 41

width: 225
zoom : 40

width: 226
zoom : 43

width: 227
zoom : 42

width: 228
zoom : 45

width: 229
zoom : 44

width: 230
zoom : 47

width: 231
zoom : 46

width: 232
zoom : 33

width: 233
zoom : 32

width: 234
zoom : 35

width: 235
zoom : 34

width: 236
zoom : 37

width: 237
zoom : 36

width: 238
zoom : 39

width: 239
zoom : 38

width: 240
zoom : 57

width: 241
zoom : 56

width: 242
zoom : 59

width: 243
zoom : 58

width: 244
zoom : 61

width: 245
zoom : 60

width: 246
zoom : 63

width: 247
zoom : 62

width: 248
zoom : 49

width: 249
zoom : 48

width: 250
zoom : 51

width: 251
zoom : 50

width: 252
zoom : 53

width: 253
zoom : 52

width: 254
zoom : 55

width: 255
zoom : 54

>>>
'''
