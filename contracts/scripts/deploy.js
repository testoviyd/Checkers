const hre = require("hardhat");

async function main() {
    const BaseCheckers = await hre.ethers.getContractFactory("BaseCheckers");
    const baseCheckers = await BaseCheckers.deploy();

    await baseCheckers.deployed();

    console.log("BaseCheckers deployed to:", baseCheckers.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
