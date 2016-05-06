# !/ bin / bash
for file in *.tar.gz
do
	dir=${file%.tar.gz}
	mkdir -p $dir
	echo "Directory $dir created"
	rm $file
	tar -xvzf $file -C $dir
	echo "Archive $file uncompressed"
done
exit 0
