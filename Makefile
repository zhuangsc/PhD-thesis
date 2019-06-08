CC=pdflatex

makepaper:
	$(CC) thesis.tex
	makeglossaries thesis
	$(CC) thesis.tex
	bibtex thesis 
	$(CC)	thesis.tex
	$(CC) thesis.tex
	
clean:
	rm -fv *.aux */*.aux *.log *.toc *.lof *.lot *.out *.blg *.bbl *.idx *.nlo *.acn *.acr *.alg *.ilg *.glo *.gls *.ind *.glg *.ist
