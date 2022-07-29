import cv2
import numpy as np
import sys,time
import mss
import threading
from pynput.mouse import Button, Controller

stc = mss.mss()
mouse = Controller()
flag = True

#posição e tamanho do print na tela
monitor = 		{
			"left": 490,
			"top": 229,
			"width": 400,
			"height": 338,
		}


def captcha_loop():
	time.sleep(8)

	#tira print
	scr = stc.grab(monitor)

	while True:

		img = np.array(scr)

		def canny(image, sigma=0.55):
			v = np.median(image)
			lower = int(max(0, (1.0 - sigma) * v)) #É o valor de limite alto do gradiente de intensidade.
			upper = int(min(255, (1.0 + sigma) * v)) #É o valor de limite Baixo do gradiente de intensidade.
			edged = cv2.Canny(image, lower, upper)
			return edged

		contours = cv2.findContours(canny(img), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

		a = 0
		for cnt in contours:
			x, y, w, h = cv2.boundingRect(cnt)
			if w >= 50 and h >= 50 and w <= 60 and h <= 60 and a == 0:
				cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
				x_1 = int(x + w / 2)
				y_1 = int(y + h / 2)
				cv2.circle(img, (x_1, y_1), 3, (0, 34, 255), -1)
				a = 1
			elif w >= 50 and h >= 50 and w <= 60 and h <= 60 and a == 1:
				cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
				x_2 = int(x + w / 2)
				y_2 = int(y + h / 2)
				distance = int(np.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2))
				cv2.circle(img, (x_2, y_2), 3, (0, 34, 255), -1)
				cv2.line(img, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
				if distance > 55:
					cv2.putText(img, str(distance), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

					def lol():
						global flag
						if x < 30:
							mouse.position = (542 + x, 533)
							time.sleep(1)
							mouse.press(Button.left)
							mouse.position = (542 + x + distance, 533)
							time.sleep(1)
							mouse.release(Button.left)
							flag = False
						elif x > 30:
							mouse.position = (542 + x - distance + 3, 533)
							time.sleep(1)
							mouse.press(Button.left)
							mouse.position = (542 + x, 533)
							time.sleep(1)
							mouse.release(Button.left)
							flag = False

					threading.Thread(target=lol).start()


		cv2.imshow('image', img)
		cv2.setWindowProperty('image', cv2.WND_PROP_TOPMOST, 1)
		flag = True
		if cv2.waitKey(1) & 0xFF == ord("q"):
			cv2.destroyAllWindows()
			cv2.waitKey(1)
			sys.exit()


if __name__ == "__main__":
	captcha_loop()