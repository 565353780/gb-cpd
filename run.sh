make OPT=-DUSE_OPENMP ENV=LINUX

./bcpd \
  -x /home/chli/chLi/Dataset/arap_test/result_xyz.txt \
  -y /home/chli/chLi/Dataset/arap_test/target_xyz.txt \
  -w 0.4 -b 0.7 -l 100 -g 3 \
  -J 300 -K 200 -p -g0.1 -ux \
  -c 1e-6 -n 500 -h -r1 \
  -G geodesic,0.2,8,0.15 \
  -o ./output/test1_ -sA
