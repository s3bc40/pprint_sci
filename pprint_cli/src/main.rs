use alloy::providers::{Provider, ProviderBuilder};
use eyre::Result;
use std::env;

#[tokio::main]
async fn main() -> Result<()> {
    // Get the command line arguments
    // The first argument is the program name, so we start from index 1
    let args: Vec<String> = env::args().collect();

    // Check the number of arguments
    match args.len() {
        1 => {
            println!("No arguments provided. Please provide a string to pretty print.");
        }
        2 => {
            let input = &args[1];
            println!("{}", input);
        }
        _ => {
            println!("Usage: {} <string>", args[0]);
        }
    }

    // Set up the HTTP transport which is consumed by the RPC client.
    let rpc_url = "https://eth.merkle.io".parse()?;

    // Create a provider with the HTTP transport using the `reqwest` crate.
    let provider = ProviderBuilder::new().on_http(rpc_url);

    // Get latest block number.
    let latest_block = provider.get_block_number().await?;

    // Print the block number.
    println!("Latest block number: {latest_block}");

    Ok(())
}
