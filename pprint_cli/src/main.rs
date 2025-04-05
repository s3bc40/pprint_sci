use std::env;

fn main() {
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
}
