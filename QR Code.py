import qrcode as qr


#simple code of making qr code 
img = qr.make("https://www.youtube.com/")  #make 
img.save("Youtube.png") # save with name as img( png )
print("You're done!")
