echo "Cloning main Repository"
git clone https://github.com/NobiDeveloper/Nobita-Filter-Bot.git /ANUSHKA
echo "DONE ✅ \n now TRYING to dEpLoY"
cd /ANUSHKA
echo "installing some apps for this bot "
pip3 install -U -r requirements.txt
echo " Successfully all applications are installed"
echo "Now Starting.... ANUSHKA"
echo "Main bot @ANUSHKA_SEN_bot"
python3 bot.py
