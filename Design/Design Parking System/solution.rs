struct ParkingSystem {
    a: Vec<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ParkingSystem {

    fn new(big: i32, medium: i32, small: i32) -> Self {
        ParkingSystem{a: vec![big, medium, small]}
    }
    
    fn add_car(&mut self, car_type: i32) -> bool {
        if self.a[(car_type - 1) as usize] == 0 {
            return false
        }
        self.a[(car_type - 1) as usize] -= 1;
        true
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */
