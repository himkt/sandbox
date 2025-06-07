use std::fs::File;
use std::io::{self, Read};

fn main() -> io::Result<()> {
    let mut file = File::open("../data/data.bin")?;
    let mut buf = [0u8; 8];

    for _ in 0..4 {
        file.read_exact(&mut buf)?;
        // buf.reverse();  // for big-endian
        println!("{:?}", buf);
        let value = i64::from_le_bytes(buf);
        println!("Parsed value: {}", value);
    }
    Ok(())
}
