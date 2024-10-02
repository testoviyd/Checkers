require("@nomiclabs/hardhat-waffle");

module.exports = {
    solidity: "0.8.0",
    networks: {
        base: {
            url: "https://base-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
            accounts: ["YOUR_PRIVATE_KEY"]
        }
    }
};
