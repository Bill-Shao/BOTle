
def getWords():
    with open('wordleanswers.txt', 'r') as f:
        lines = f.readlines()
    lines = [lines[i].split("\t")[2] for i in range(1,len(lines))]
    return lines
def allCombos():
    return ['GGGGG', 'GGGGY', 'GGGGB', 'GGGYG', 'GGGYY', 'GGGYB', 'GGGBG', 'GGGBY', 
    'GGGBB', 'GGYGG', 'GGYGY', 'GGYGB', 'GGYYG', 'GGYYY', 'GGYYB', 'GGYBG', 'GGYBY',
     'GGYBB', 'GGBGG', 'GGBGY', 'GGBGB', 'GGBYG', 'GGBYY', 'GGBYB', 'GGBBG', 'GGBBY',
      'GGBBB', 'GYGGG', 'GYGGY', 'GYGGB', 'GYGYG', 'GYGYY', 'GYGYB', 'GYGBG', 'GYGBY',
       'GYGBB', 'GYYGG', 'GYYGY', 'GYYGB', 'GYYYG', 'GYYYY', 'GYYYB', 'GYYBG', 'GYYBY',
        'GYYBB', 'GYBGG', 'GYBGY', 'GYBGB', 'GYBYG', 'GYBYY', 'GYBYB', 'GYBBG', 'GYBBY',
         'GYBBB', 'GBGGG', 'GBGGY', 'GBGGB', 'GBGYG', 'GBGYY', 'GBGYB', 'GBGBG', 'GBGBY',
          'GBGBB', 'GBYGG', 'GBYGY', 'GBYGB', 'GBYYG', 'GBYYY', 'GBYYB', 'GBYBG', 'GBYBY',
           'GBYBB', 'GBBGG', 'GBBGY', 'GBBGB', 'GBBYG', 'GBBYY', 'GBBYB', 'GBBBG', 'GBBBY',
            'GBBBB', 'YGGGG', 'YGGGY', 'YGGGB', 'YGGYG', 'YGGYY', 'YGGYB', 'YGGBG', 'YGGBY',
             'YGGBB', 'YGYGG', 'YGYGY', 'YGYGB', 'YGYYG', 'YGYYY', 'YGYYB', 'YGYBG', 'YGYBY',
              'YGYBB', 'YGBGG', 'YGBGY', 'YGBGB', 'YGBYG', 'YGBYY', 'YGBYB', 'YGBBG', 'YGBBY',
               'YGBBB', 'YYGGG', 'YYGGY', 'YYGGB', 'YYGYG', 'YYGYY', 'YYGYB', 'YYGBG', 'YYGBY',
                'YYGBB', 'YYYGG', 'YYYGY', 'YYYGB', 'YYYYG', 'YYYYY', 'YYYYB', 'YYYBG', 'YYYBY',
                 'YYYBB', 'YYBGG', 'YYBGY', 'YYBGB', 'YYBYG', 'YYBYY', 'YYBYB', 'YYBBG', 'YYBBY',
                  'YYBBB', 'YBGGG', 'YBGGY', 'YBGGB', 'YBGYG', 'YBGYY', 'YBGYB', 'YBGBG', 'YBGBY',
                   'YBGBB', 'YBYGG', 'YBYGY', 'YBYGB', 'YBYYG', 'YBYYY', 'YBYYB', 'YBYBG', 'YBYBY',
                    'YBYBB', 'YBBGG', 'YBBGY', 'YBBGB', 'YBBYG', 'YBBYY', 'YBBYB', 'YBBBG', 'YBBBY',
                     'YBBBB', 'BGGGG', 'BGGGY', 'BGGGB', 'BGGYG', 'BGGYY', 'BGGYB', 'BGGBG', 'BGGBY',
                      'BGGBB', 'BGYGG', 'BGYGY', 'BGYGB', 'BGYYG', 'BGYYY', 'BGYYB', 'BGYBG', 'BGYBY',
                       'BGYBB', 'BGBGG', 'BGBGY', 'BGBGB', 'BGBYG', 'BGBYY', 'BGBYB', 'BGBBG', 'BGBBY',
                        'BGBBB', 'BYGGG', 'BYGGY', 'BYGGB', 'BYGYG', 'BYGYY', 'BYGYB', 'BYGBG', 'BYGBY',
                         'BYGBB', 'BYYGG', 'BYYGY', 'BYYGB', 'BYYYG', 'BYYYY', 'BYYYB', 'BYYBG', 'BYYBY',
                          'BYYBB', 'BYBGG', 'BYBGY', 'BYBGB', 'BYBYG', 'BYBYY', 'BYBYB', 'BYBBG', 'BYBBY',
                           'BYBBB', 'BBGGG', 'BBGGY', 'BBGGB', 'BBGYG', 'BBGYY', 'BBGYB', 'BBGBG', 'BBGBY',
                            'BBGBB', 'BBYGG', 'BBYGY', 'BBYGB', 'BBYYG', 'BBYYY', 'BBYYB', 'BBYBG', 'BBYBY',
                             'BBYBB', 'BBBGG', 'BBBGY', 'BBBGB', 'BBBYG', 'BBBYY', 'BBBYB', 'BBBBG', 'BBBBY',
                              'BBBBB']
    