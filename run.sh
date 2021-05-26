pytest -v -s -m "sanity" --capture=sys --html=Reports/chrome_sanity_report.html testCases/ --browser chrome
pytest -v -s -m "regression" --capture=sys --html=Reports/firefox_regression_report.html testCases/ --browser firefox
#pytest -v -s -m "regression" --capture=sys --html=Hybridframework/nopcommerceApp/Reports/sanity_report.html Hybridframework/nopcommerceApp/testCases/ --browser chrome
#pytest -v -s -m "sanity and regression" --capture=sys --html=Hybridframework/nopcommerceApp/Reports/sanity_report.html Hybridframework/nopcommerceApp/testCases/ --browser chrome