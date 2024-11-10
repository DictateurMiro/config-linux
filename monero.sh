sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
sed -i 's/constexpr const int kDefaultDonateLevel = 1;/constexpr const int kDefaultDonateLevel = 0;/g; s/constexpr const int kMinimumDonateLevel = 1;/constexpr const int kMinimumDonateLevel = 0;/g' /home/miro/xmrig/src/donate.h
cmake ..
make -j$(nproc)
curl -o /home/miro/config.json https://raw.githubusercontent.com/DictateurMiro/config-linux/refs/heads/main/config.json
