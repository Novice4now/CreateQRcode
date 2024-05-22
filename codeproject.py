import segno

qrcode = segno.make('I love apprenticeships')
qrcode.save('apprenticeships.png',
            dark='darkgreen',
            light='lightblue',
            scale=10)

