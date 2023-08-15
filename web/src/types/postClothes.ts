import { Gender } from './gender';

export interface PostClothes {
  category: string;
  cloth_type: string;
  max_temp: number;
  min_temp: number;
  gender: Gender;
  image?: null;
}

export interface ErrorClothes {
  category: string;
  cloth_type: string;
  max_temp: string;
  min_temp: string;
  gender: string;
  image?: string;
}
